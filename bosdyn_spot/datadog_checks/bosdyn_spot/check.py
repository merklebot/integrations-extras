import bosdyn.client
from bosdyn.client.robot_state import RobotStateClient
from datadog_checks.base import AgentCheck, ConfigurationError

from bosdyn.client.exceptions import UnableToConnectToRobotError
from bosdyn.client.auth import InvalidLoginError

class BosdynSpotCheck(AgentCheck):
    __NAMESPACE__ = 'bosdyn_spot'

    def __init__(self, name, init_config, instances):
        super(BosdynSpotCheck, self).__init__(name, init_config, instances)

        self.spot_address = self.instance.get("spot_address")
        self.spot_user = self.instance.get("spot_user")
        self.spot_password = self.instance.get("spot_password")

    def _ensure_spot_conn(self):
        self.spot_sdk = bosdyn.client.create_standard_sdk("DatadogAgent")
        self.spot = self.spot_sdk.create_robot(self.spot_address)
        self.spot.authenticate(self.spot_user, self.spot_password)
        self.spot_state_client = self.spot.ensure_client(RobotStateClient.default_service_name)

    def check(self, _):
        try:
            self._ensure_spot_conn()
        except InvalidLoginError as e:
            self.service_check("can_connect", AgentCheck.CRITICAL, message=str(e))
            raise ConfigurationError('Invalid Credentials, please, fix configuration')

        except Exception as e:
            # import traceback
            # traceback.print_exc()
            self.service_check("can_connect", AgentCheck.CRITICAL, message=str(e))
            return

        try:
            self.service_check("can_connect", AgentCheck.OK)
            state = self.spot_state_client.get_robot_state()
            metrics = self.spot_state_client.get_robot_metrics()
            self.gauge("battery_states.0.charge_percentage", state.battery_states[0].charge_percentage.value)
            for metric in metrics.metrics:
                if metric.label == "distance":
                    self.gauge("metrics.distance_m", metric.float_value)
                break
        except Exception as e:
            self.service_check("can_connect", AgentCheck.CRITICAL, message=str(e))