# Functions

## Anonymous vs Named Functions

## IIFE

## Closures
A closure is when a function is bundled together with its surrounding environment. The closure gives you access to the parent/outer function's scope. 
Closures are created every time a function is created.

```js

function getData(url) {
  fetch(url).then(() => {
    // .then callback is an anonymous function which handles the response
    //  it will have access to the scope of getData,
    //  even if getData does not exist anymore, because of the 
    console.log(url)
  })
}

getData('https://some-url.com')

```

### `let` vs `var` vs `const`
When you declare a variable with `let`, you are creating a *block-scoped* variable.
```js

let x = 1

if (x === 1) {
  let x = 2
  console.log(x) // 2
}
console.log(x) // 1

```
Declaring a variable with `const` sees that the value is block-scoped, but the value cannot be reassigned, as it is a *constant*. 
Arrays and objects are still mutable, but they cannot be reassigned.

Declaring a variable with `var` creates a *function-scoped* or *global* variable.
```js
var message = 'Hello world'

console.log(message) // Hello World

if (true) {
  var message = 'Goodbye world'
}

console.log(message) // Goodbye world
```
