## 1. Fine-tuned AI model

- Don't explain WHAT it should do. SHOW it.
- 20 - 50 GOOD examples from you or other content
- Reverse engineer the prompt

```md
## PROMPT

<!-- we can ask chat GPT to reverse engineer it -->
<write what the prompt would have looked like>

## POST

<the content>
```

- After you've gathered the posts you like, convert them to `jsonl` in this format:

```json
{
  "messages": [
    { "role": "user", "content": "--prompt--" },
    { "role": "assistant", "content": "--reply--" }
  ]
}
```

- Then, go to open AI into the finetune path and upload our json
  https://platform.openai.com/finetune

- Once it's ready, to go `playground`

## 2. Create a brand brief

- While the part 1 makes sure the model sounds like you, the part 2 is about saying things you'd say.
- Part 1 is about writing style, and part 2 is about core beliefs to adopt
- Beliefs, themes, hot-takes, values to align with

## 3. Create AI agents

- Idea generator
- Content writer
- Refiner/Editor

Identify what should be the input shape on the workflow

> Notion integration:"
