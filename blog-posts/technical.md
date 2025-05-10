# Sources

- https://www.robinwieruch.de/
- https://kentcdodds.com/blog
- https://leerob.com/
- https://overreacted.io/ : dan's blog
  https://www.joshwcomeau.com/ - amazing blog

# Post 1

## React vs Next.js - Please Stop Treating Them Like They’re Interchangeable

I see it all the time: “Hiring React/Next.js Developer”, as if they’re the same thing.

They’re not. And they were never meant to be used interchangeably.

### Breaking It Down

React is a JavaScript library for building UIs.

It handles rendering components on the client side (CSR).
You choose your own router, state manager, bundler, it's unopinionated and flexible.

Use it when you're building a single-page application (SPA), dashboards, internal tools, or any app where SEO isn’t a priority. React gives you the freedom to pair it with any backend (like Node.js) and structure your app as you see fit.

---

Next.js, on the other hand, is a framework built on top of React. It comes with:

File-based routing (no need for React Router)
Built-in SSR (Server-Side Rendering) for SEO
SSG (Static Site Generation) for fast content delivery
API routes (basic backend logic inside the frontend project)
Built-in image optimization and performance tooling

Next.js is ideal for SEO-sensitive or public-facing apps like eCommerce, blogs, landing pages, and hybrid websites.

React and Next differences

### Why the Distinction Matters

A React front-end developer might not know how to work with SSR, server-side lifecycles, or file-based routing since these are generally backend functions. A Next.js developer needs to understand both frontend React logic and backend request handling, especially when dealing with dynamic rendering or API routes.

And here's where it gets even more important:

React and Next still use Node.js

### Next.js Does Not Replace Node.js

It simply offloads some backend responsibilities for specific types of projects.

If you’re building a complex app, you’ll likely still need a dedicated Node.js backend for authentication, database interactions, real-time data, microservices, etc.

In fact, most of what Next.js offers SSR, routing, APIs can be done using React + Node.js manually, with more flexibility and control.

So no, you don’t just swap stacks based on what’s trending.

You pick the right tool for the right job.

### Practical Perspective

Here’s how I see it:

- React: You want flexibility, control, and you're building a client-heavy SPA with a custom backend like Node.js.
- Next.js: You want faster setup, built-in SSR/SSG, and you're building something that benefits from tight frontend-backend coupling and SEO optimization.

Before posting your next job listing or scoping your next project, ask yourself:

> What are we actually building and what does the stack need to support?

Tech is a toolbox. React is a tool. Next.js is a toolbox built around it. Node.js is still the workbench underneath it all.

Use the right one.

# Post 2

## React Best Practices Ever Developer Should Know

The more I study React.js, the more I fall in love with it. No doubt that it’s one of the most useful and loved front-end JavaScript libraries out there. And the improvements that the React team have made lately don’t just affect developers, but also those who use applications built with React.

In a previous article, I talked about various React Hooks and how they work along with code samples and detailed explanations.

In this guide, I’m going to talk about some important things that I’ve learned while developing React apps. And these learnings are optimized based on using React Hooks. We’ll debunk some common myths, simplify common concepts, and optimize your code for the best performance.

What we’ll cover:

- How Will This Guide Benefit You?
- Prerequisites
- React State Must Be Immutable
- Don't Use State for Everything
- Derive Values Without State
- Compute Values Without Effects
- Keys Should Be Unique
- Use useEffect Last

## How Will This Guide Benefit You?

Let’s say you have a knife and I ask you to cut out some shapes from a piece of cloth. You could do it, but it would take a while and be challenging using a knife. Instead, what if I gave you a pair of really sharp scissors and then asked you to cut out the patterns? It’d be much easier, right?

This guide is like that optimised approach of cutting cloth with scissors instead of a knife. I’ll teach you how to use React more easily, without as much struggle. We’ll discuss the important aspects of how React Hooks work, and we’ll also cover some do’s & don’ts.

## Prerequisites

There is only one main prerequisite for following this guide: you should have used React hooks at least once. And by this I mean developed an application with React that leverages the power of hooks.

This article is for everyone who wishes to use React hooks to their full potential.

## React State Must Be Immutable

Have you ever wondered why React makes such a fuss about immutability? 🤔 As a newbie, you might think that JavaScript's mutations are perfectly fine. After all, we add or remove properties from objects and manipulate arrays with ease.

But here's the twist: in React, immutability isn't about never changing state, it's about ensuring consistency.

When you mutate state directly, React can’t detect changes reliably. This means your UI might not update as expected. The trick? Replace old data with new copies.

For instance, if you need to add a user, you should create a new array with the new user included, rather than pushing directly into the existing array.

```jsx
const updatedUsers = [...users, newUser];
```

The code `const updatedUsers = [...users, newUser]`; uses the spread operator to create a new array, `updatedUsers`, which combines the existing users with `newUser`.

This approach maintains immutability in React by not modifying the original users array. Instead, it creates a new state representation, allowing React to optimize rendering and ensure predictable state changes. When you update the state using `setUsers(updatedUsers)`;, React re-renders the component based on this new array, adhering to best practices for state management.

This ensures React detects the change and re-renders your component smoothly.

## Don't Use `useState` for Everything

Confession time: I used to throw everything into `useState` without thinking twice. 🚀 But here's the scoop: not everything needs to be in state. The state is powerful, but overusing it can lead to complex and inefficient code.

Consider alternatives like server state, URL state, or local storage. For server data, libraries like React Query are a game changer. They handle fetching and caching so you don’t have to manage it manually. For URL state, leverage hooks like useLocation from React Router or Next.js’s built-in methods.

Checklist before using useState:

Is this value simple and derivable during render?

Does a library already manage this state?

Does it need to trigger a re-render?

If you answer “no” to all, you might not need useState at all.

Derive Values Without State
Here’s a little-known trick: Derived values don't need to live in state. 🚀 If your data can be computed from existing states or props, calculate it directly during render.

For example, formatting a date can be done on the fly without additional hooks:

const formattedDate = new Date(date).toLocaleDateString();
The code const formattedDate = new Date(date).toLocaleDateString(); derives a formatted date string from a given date input without storing it in the component's state. By creating formattedDate as a constant, it calculates the value on the fly each time it's called, reflecting the current state of date.

This approach avoids unnecessary state management, simplifies rendering logic, and keeps the component efficient, as derived values are recalculated only when the underlying data changes. Thus, it promotes a clean, functional style of programming in React

This keeps your components clean and avoids unnecessary state updates.

Compute Values Without Effects
Stop using useEffect for simple computations! 🛑 If your value can be calculated directly from state or props and doesn’t involve side effects, do it during render. For expensive computations, wrap them in useMemo to optimize performance:

const expensiveValue = useMemo(() => computeExpensiveValue(data), [data]);This reduces the complexity of your code and keeps your components focused.
The code const expensiveValue = useMemo(() => computeExpensiveValue(data), [data]); uses the useMemo hook to compute a value (expensiveValue) based on the data input without triggering side effects.

It memoizes the result of computeExpensiveValue(data), recalculating it only when data changes. This approach prevents unnecessary recalculations on every render, enhancing performance for expensive computations.

By relying on useMemo, the component efficiently derives the value based on its current props or state, keeping the rendering process efficient and focused on the latest data.

Keys Should Be Unique
Guilty as charged: I’ve used array indexes as keys in lists before. 😅 But did you know this can lead to bugs? React relies on unique keys to identify items, and using non-unique values can mess things up.

Generate unique IDs using crypto.randomUUID() but make sure to do it only when your state updates, not on every render. For objects, consider adding an id property:

const itemWithId = items.map(item => ({ ...item, id: generateUniqueId() }));
The code const itemWithId = items.map(item => ({ ...item, id: generateUniqueId() })); creates a new array, itemWithId, where each item in the items array is augmented with a unique id.

The spread operator (...item) copies the properties of each item, while generateUniqueId() generates a new, unique identifier. This ensures that each item has a distinct key, which is crucial for React components when rendering lists.

Unique keys help React efficiently manage updates, identify changes, and optimize rendering performance by distinguishing between different list items.

Don't Leave Out Dependencies
One of React’s cruel quirks: Forgetting dependencies in useEffect can lead to stale closures. 😱 For example, if you useEffect doesn’t include the dependencies it needs, it might not update as expected.

Always double-check your dependency arrays:

useEffect(() => {// Effect logic}, [dependency]);
The code useEffect(() => { /_ Effect logic _/ }, [dependency]); defines a side effect in a React component that runs when the specified dependency changes. It's essential to include all relevant dependencies in the dependency array to ensure that the effect behaves correctly.

Omitting dependencies can lead to stale or incorrect values being used in the effect, as React may not re-run it when needed. Including all dependencies helps maintain synchronization between the component's state and the effect, ensuring predictable behaviour and preventing potential bugs related to missed updates.

If your UI isn’t updating correctly, this is often the culprit.

Use useEffect Last
Here’s a pro tip: Don’t rush to use useEffect. 🙅‍♂️ It’s powerful but can lead to messy code if overused. React frameworks provide solutions to manage side effects more elegantly. For data fetching, consider libraries like TanStack Query or SWR that handle requests and caching efficiently, leading to a better user experience.

Alternative strategies:

Derive values directly.

Respond to events with handlers.

Fetch data on the server or with dedicated libraries.

Conclusion
React is a robust library, but knowing how to use it effectively can make all the difference. These lessons are just the beginning.

Having an in-depth idea about in and outs of any technology helps you during development and optimization.

React Js is the perfect library for modern development it has everything to offer for development and optimization

Thanks for reading, and happy coding! 🎉
