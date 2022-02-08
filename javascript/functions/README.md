# Functions
JavaScript is unlike any other language in regards to functions. There are many different ideas to keep in mind when working with functions.

## Function declaration
Function declaration requires a function name.
<pre>
<b>function [functionName]</b> (arg1, arg2) {
  // function body
}
</pre>

```js
function sayMyName(name) {
  console.log(name)
}
```

## Function Expressions
Variables can be assigned function expressions. Function expressions don't need to be named, because they are an expression rather than a declaration.
<pre>
<b>const [variableName]</b> = <b>function</b> () {}
</pre>

Or,
<pre>
<b>const [variableName]</b> = <b>function [functionName]</b> () {}
</pre>

## Named Functions

A function is **named** if it has been given a name after the `function` keyword, e.g.
```js
function sum(a, b) {
  return a + b
}
```

## Anonymous Functions

An anonymous function has no name. Function expressions which have no name after the `function` keyword are anonymous.
```js
const sayMyName = function(name) {
  console.log(name)
}
```
In this case, `sayMyName` is a *variable*, whose initial value is a function.

### Arrow functions
Are anonymous functions. Also known as lamba functions.

```js
const sayMyName = (name) => {
  console.log(name)
}
```

## IIFE
Immediately Invoked Function Expressions, are function expressions which are invoked or called immediately. They can be named or unnamed.
It is recommended to name IIFEs, for reasons I will get into soon.

```js
(function sayMyName(name) {
  console.log(name) // Sean
}) ("Sean")
```

## Stack Trace


# Closures
A closure is the environment surrounding a function. Whenever a function is created, it is bundled together with references to required variables in the upper scope. The closure gives you access to the parent/outer function's scope, even if the parent function has closed. 

```js

function getData(url) {
  // Since fetch usually takes a while, the .then callback will likely be called when getData has closed.
  
  const test = 'Hello world'
  
  fetch(url).then(() => {
    // .then callback is an anonymous function which handles the response
    //  it will have access to the scope of getData,
    //  even if getData has closed
    // This anonymous function exists separately from getData, and is bundled with any necessary variables from the outer function (url)
    console.log(url, test)
  })
}

getData('https://some-url.com')

```

In the below example, we have a nested function which is returned when `counter` is called. We need to initialise a variable, `count`, to `counter()` in order to access the return function, and `count` becomes a function. Since `initialValue` is used in this return function, a reference will be kept so we can keep incrementing and accessing it via `count()`

```js
function counter(initialValue) {
  console.log('Counter initialised with value ', initialValue)

  return function() {
    console.log('Counter value: ', ++initialValue)
  }
}

const count = counter(2) // Outputs: Counter initialised with value 2

// Even though the lifecycle of counter() has ended, we can still access initialValue
count() // Outputs: Counter value: 3
count() // Outputs: Counter value: 4

```

# Hoisting
Hoisting is the behaviour of moving declarations to the top of the file. 

`var`s can be used before they are initialised, while `let`s cannot.

```js

console.log(x) // returns undefined
console.log(y) // ReferenceError

var x = 1
let y = 2

```

Named functions can also be invoked before they are declared. Anonymous functions **cannot** be invoked before they are declared.

```js
test() // Output: "Test"
test2() // ReferenceError

function test() {
  console.log('Test')
}

const test2 = () => {
  console.log('Test2')
}
```

# Scope
The scope determines accessibility of variables.

## Global Scope
At the top of a js file, you may declare a variable. This variable is now global, and can be accessed in any block/function.
```js
// global scope
let x = 12

function saySomething() {
  // function scope (local)
  console.log(x) // prints 12
}

if (true) {
  // block scope (local)
  console.log(x) // prints 12
}
```

## Function Scope
Variables with function scope cannot be accessed from outside that function.
```js
function createVariable() {
  // Function scope...
  let x = 12
}

createVariable()

console.log(x) // ReferenceError

```

## Block Scope
Variables with block scope cannot be referenced outside of the block of code which declared it.

```js

if (true) {
  // Block scope
  let x = 4
}

console.log(x) // ReferenceError

```

## `let` vs `var` vs `const`
| statement | scope | initialised? | can redeclare? |
| --- | --- | --- | --- |
| `var` | function scope | undefined | yes |
| `let` | block scope | not initialised | no |
| `const` | block scope | not initialised | no |

`let` and `const` are block scoped. Trying to reference them outside of the block will cause an error.
On the other hand, `var` is function scoped. Referencing this outside of the `if` block is fine, but outside of a function will cause an error.
```js

if (true) {
  var x = 11
  let y = 12
  const z = 13
}

function declareA() {
  var a = 14
}

console.log(x) // 11
console.log(y) // ReferenceError
console.log(z) // ReferenceError
console.log(a) // ReferenceError

```
