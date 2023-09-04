```
ageError.json
```
```json
{
  "messageVersion": "1.0",
  "invocationSource": "DialogCodeHook",
  "userId": "John",
  "sessionAttributes": {},
  "bot": {
    "name": "RoboAdvisor",
    "alias": "$LATEST",
    "version": "$LATEST"
  },
  "outputDialogMode": "Text",
  "currentIntent": {
    "name": "recommendPortfolio",
    "slots": {
      "firstName": "John",
      "age": "67",
      "riskLevel": "Low",
      "investmentAmount": "5000"
    },
    "confirmationStatus": "None"
  }
}
```
```
correctDialog.json
```
```json
{
  "messageVersion": "1.0",
  "invocationSource": "DialogCodeHook",
  "userId": "John",
  "sessionAttributes": {},
  "bot": {
    "name": "RoboAdvisor",
    "alias": "$LATEST",
    "version": "$LATEST"
  },
  "outputDialogMode": "Text",
  "currentIntent": {
    "name": "recommendPortfolio",
    "slots": {
      "firstName": "John",
      "age": "40",
      "riskLevel": "Low",
      "investmentAmount": "5000"
    },
    "confirmationStatus": "None"
  }
}
```
```
incorrectAmountError.json
```
```json
{
  "messageVersion": "1.0",
  "invocationSource": "DialogCodeHook",
  "userId": "John",
  "sessionAttributes": {},
  "bot": {
    "name": "RoboAdvisor",
    "alias": "$LATEST",
    "version": "$LATEST"
  },
  "outputDialogMode": "Text",
  "currentIntent": {
    "name": "recommendPortfolio",
    "slots": {
      "firstName": "John",
      "age": "40",
      "riskLevel": "Low",
      "investmentAmount": "500"
    },
    "confirmationStatus": "None"
  }
}
```
```
negativeAgeError.json
```
```json
{
  "messageVersion": "1.0",
  "invocationSource": "DialogCodeHook",
  "userId": "John",
  "sessionAttributes": {},
  "bot": {
    "name": "RoboAdvisor",
    "alias": "$LATEST",
    "version": "$LATEST"
  },
  "outputDialogMode": "Text",
  "currentIntent": {
    "name": "recommendPortfolio",
    "slots": {
      "firstName": "John",
      "age": "-2",
      "riskLevel": "Low",
      "investmentAmount": "5000"
    },
    "confirmationStatus": "None"
  }
}
```