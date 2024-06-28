# An AI chat app made with Flet

A small and customisable app programmed in flet to chat with chatgpt via the openai interface. Easily customisable, clearly understandable.

![AI Chat](screenshot.png)

First add a file named .env with your [Open-AI-Key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)!

`OPENAI_API_KEY=sk-proj-...`

To run the app:

```
pip install flet
flet run 
```
I have found that newer versions of Flet do not work on the Mac. Version 0.22.0 works for me:

```
pip install flet==0.22.0
```

Build the app:

```
flet build macos 
```