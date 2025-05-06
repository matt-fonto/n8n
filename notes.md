# n8n

- low-code automation tool
- allow workflow build
- benefits of automating workflows
  - increased efficiency
  - time & cost savings
  - scalability
  - improved data handling
  - enhanced customer experience

## n8n workflow ideas

- Automated lead enrichment + CRM sync
- Newsletter curation assistant
- Job monitoring & alert system
- Custom social media automation
- Client onboarding

## n8n interface

- Workflow: the recipe
- Nodes: Each step, each ingredient
- Execution: when an order comes in

## core concepts

### types of nodes

- triggers
  - what they do: tell n8n when/how to start the workflow
  - types: manual, scheduled, on chat, on event, called by another workflow
- action
  - what they do: the "doers", they perform specific tasks
  - types: send email, create record, make api request, get text messages, set calendar event, etc
- data transformation
  - what they do: change or process the data flowing through
  - types:
    - set: add fields, change values, reduce data
    - aggregate: combines data into a single output
    - merge: combining data from two sources
- logic
  - what they do: conditional decision makers
  - types:
    - if
    - switch
    - wait
- first workflow

## setup docker mac n8n

![alt text](image.png)

<!-- to continue: 23:20 -->

https://www.youtube.com/watch?v=ZHH3sr234zY&list=PLFbXZOeg7GKZdj0IvSrln2WbrJh54ci25&index=16

## google oauth

- setup the connection by:

1. add the oauth redirect url to google cloud
2. app will initially be on testing, you should add yourself as test users

- go to audience/test users/add your email

![alt text](image-1.png) 3. add secret and client id to the integration

## setting up AI

- Create a node: chat with model
- Setup the credentials
- Add a message -- you can add multiple. This is like the prompt.

  - Here you can tell the message how to behave. There are 3 options:
  - User: similar to the experience of the chat
  - Assistant: shapes the style (tone/personality) of the AI
  - System: shapes the behavior of the AI. Also used to specify output

  ![alt text](image-2.png)

- Then, drag and drop the fields into the prompt to make them variables

![alt text](image-3.png)

- Once the execution is fine, click in activating it
