# azure-baremetalinfrastructure-cli-extension

# Install

To install this extension just use the CLI extension add command:

```
az extension add --source $LATEST_RELEASE
```

# Usage

To list all BareMetal instances for the subscription:

```
az baremetalinstance list
```

To show details about a specific BareMetal instance:

```
az baremetalinstance show --resource-group $RESOURCE_GROUP --instance-name $BM_INSTANCE_NAME
```

To add a key-value pair to the Tags field of a specific BareMetal instance:

```
az baremetalinstance update --resource-group $RESOURCE_GROUP --instance-name $BM_INSTANCE_NAME --set tags.newKey=value
```

To update a key-value pair in the Tags field of a specific BareMetal instance:

```
az baremetalinstance update --resource-group $RESOURCE_GROUP --instance-name $BM_INSTANCE_NAME --set tags.key=updatedValue
```

To delete a key-value pair from the Tags field of a specific BareMetal instance:

```
az baremetalinstance update --resource-group $RESOURCE_GROUP --instance-name $BM_INSTANCE_NAME --remove tags.key
```

To delete all key-value pairs in the Tags field of a specific BareMetal instance:

```
az baremetalinstance update --resource-group $RESOURCE_GROUP --instance-name $BM_INSTANCE_NAME --set tags={}
```

To delete a BareMetal instance:

```
az baremetalinstance delete --resource-group $RESOURCE_GROUP --instance-name $BM_INSTANCE_NAME
```

To start a specific BareMetal instance:

```
az baremetalinstance start --resource-group $RESOURCE_GROUP --instance-name $BM_INSTANCE_NAME
```

To restart a specific BareMetal instance:

```
az baremetalinstance restart --resource-group $RESOURCE_GROUP --instance-name $BM_INSTANCE_NAME
```

To force restart a specific BareMetal instance:

```
az baremetalinstance restart --resource-group $RESOURCE_GROUP --instance-name $BM_INSTANCE_NAME --force
```

To shutdown a specific BareMetal instance:

```
az baremetalinstance shutdown --resource-group $RESOURCE_GROUP --instance-name $BM_INSTANCE_NAME
```

# Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
