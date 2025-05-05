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
