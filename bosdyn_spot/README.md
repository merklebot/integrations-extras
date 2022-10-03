# Agent Check: bosdyn_spot

## Overview

This check monitors [bosdyn_spot][1].

## Setup

### Installation

To install the bosdyn_spot check on your host:


1. Install the [developer toolkit]
(https://docs.datadoghq.com/developers/integrations/new_check_howto/#developer-toolkit)
 on any machine.

2. Run `ddev release build bosdyn_spot` to build the package.

3. [Download the Datadog Agent][2].

4. Upload the build artifact to any host with an Agent and
 run `datadog-agent integration install -w
 path/to/bosdyn_spot/dist/<ARTIFACT_NAME>.whl`.

### Configuration

1. <List of steps to setup this Integration>

### Validation

<Steps to validate integration is functioning as expected>

## Data Collected

### Metrics

bosdyn_spot does not include any metrics.

### Service Checks

bosdyn_spot does not include any service checks.

### Events

bosdyn_spot does not include any events.

## Troubleshooting

Need help? Contact [Datadog support][3].

[1]: **LINK_TO_INTEGRATION_SITE**
[2]: https://app.datadoghq.com/account/settings#agent
[3]: https://docs.datadoghq.com/agent/kubernetes/integrations/
[4]: https://github.com/DataDog/integrations-extras/blob/master/bosdyn_spot/datadog_checks/bosdyn_spot/data/conf.yaml.example
[5]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[6]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[7]: https://github.com/DataDog/integrations-extras/blob/master/bosdyn_spot/metadata.csv
[8]: https://github.com/DataDog/integrations-extras/blob/master/bosdyn_spot/assets/service_checks.json
[9]: https://docs.datadoghq.com/help/

