import requests
import xml.etree.ElementTree as ET

# Define Class


class QuestionsExplorer:
    def GetQuestions(self, questionType, userInput, countryCode):
        questionResults = []
        # Build Google Search Query
        searchQuery = questionType + " " + userInput + " "
        # API Call
        googleSearchUrl = "http://google.com/complete/search?output=toolbar&gl=" + \
            countryCode + "&q=" + searchQuery

        # Call The URL and Read Data
        result = requests.get(googleSearchUrl)
        tree = ET.ElementTree(ET.fromstring(result.content))
        root = tree.getroot()
        for suggestion in root.findall('CompleteSuggestion'):
            question = suggestion.find('suggestion').attrib.get('data')
            questionResults.append(question)

        return questionResults


# Get a Keyword From The User
userInput = input("Enter a Keyword: ")

# Create Object of the QuestionsExplorer Class
qObj = QuestionsExplorer()

# Call The Method and pass the parameters
questions = qObj.GetQuestions("is", userInput, "us")

# Loop over the list and pring the questions
for result in questions:
    print(result)


print("Done")
