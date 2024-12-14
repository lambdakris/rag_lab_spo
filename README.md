# RAG Lab for SharePoint Online

## Prereqs

To work with this repo you need:

- VS Code
- Git
- Github
- Astral UV
- Azure subscription
- Microsoft 365 Work or School account with Global Administrator role
  - SharePoint only comes with Work or School accounts
  - If you don't have a Work or School account with sufficient access, you can:
    - Open a Microsoft 365 Work account with a 30 day trial
    - Apply for a Microsoft 365 Developer account

## Setup

### Register Application within Microsoft Entra

1. Open a browser and navigate to the [Microsoft Entra admin center](https://entra.microsoft.com/) and login using a Microsoft 365 Account.

1. From the left hand menu, click on Identity > Applications > App registrations.

1. Click on New registration.

1. Enter a name for your application, for example, rag_lab_spo.

1. Under Supported account types, select Accounts in this organizational directory only.

1. Leave Redirect URI alone.

1. Select Register.

1. On the App Registration Overview page, copy the value of the Application (client) ID and Directory (tenant) ID and save them for later.

### Configure Permissions within Microsoft Entra

1. Select API permissions under Manage.

1. Remove the default User.Read permission under Configured permissions by selecting the ellipses (...) in its row and selecting Remove permission.

1. Select Add a permission, then Microsoft Graph.

1. Select Application permissions.

1. Select User.Read.All, then select Add permissions.

1. Select Grant admin consent for..., then select Yes to provide admin consent for the selected permission.

1. Select Certificates and secrets under Manage, then select New client secret.

1. Enter a description, choose a duration, and select Add.

1. Copy the secret from the Value column, you will need it in the next steps.

## 

## References

https://github.com/microsoftgraph/msgraph-training-python/tree/main/app-auth
https://github.com/microsoftgraph/msgraph-sdk-python
https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
