#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "8958f321-de6e-4cee-bf26-e2468b5f381f")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "76124e241f8f44f291083991eb6da19b")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://flymebot-authoring.cognitiveservices.azure.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "InstrumentationKey=18d2abda-0cb2-4296-989d-a5a33ab093f9;IngestionEndpoint=https://westus2-2.in.applicationinsights.azure.com/;LiveEndpoint=https://westus2.livediagnostics.monitor.azure.com/"
    )
