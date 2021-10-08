# The JS Event Loop

---

["The event loop is the secret behind JavaScript's asynchronous programming."](https://www.educative.io/edpresso/what-is-an-event-loop-in-javascript)

![JS Event Loop](https://miro.medium.com/max/1400/1*_x4mkpWcBs72s5BcdJe4Wg.png)
_image via [Medium](https://medium.com/nerd-for-tech/the-call-stack-and-memory-heap-explained-e50450aa1274)_

## Call Stack

Follows the [stack data structure](../../cs/data%20structures/README.md), a first-come-last-served structure (first-in last-out). It is responsible for maintaining the flow of execution in a program. Simple variables may be stored in the stack depending on the JavaScript engine.

## Message Queue / Callback Queue

This follows the [queue data structure](../../cs/data%20structures/README.md). Similar to a queue in real life, it's first-come-first-served (first-in first-out). Messages are associated with callbacks to perform actions. The first message to get pushed to the queue is the first message to get executed.

Whenever the window is resized by the user, the anonymous function below gets pushed to the message queue.

```js
window.addEventListener('resize', () => {
	console.log('resize!')
})
```

## Memory Heap

Objects are stored in the heap when defined. This sort of heap differs to the **data structure**. The heap is where dynamically allocated memory is stored, like when using [`malloc()`](http://www.cplusplus.com/reference/cstdlib/malloc/) in _C_ or _C++_. Memory allocated to the heap will remain there until the memory is freed, or the program terminates.

As JavaScript is written in _C++_, new JS objects are allocated to the heap via [`malloc()`](http://www.cplusplus.com/reference/cstdlib/malloc/). As opposed to low-level languages, where memory needs to be freed manually, JavaScript implements automatic memory management, also known as _garbage collection_

## Event Loop

Is a loop which runs throughout the program lifecycle. It waits for a message to arrive from the Message Queue, and executes it. Each message is processed completely before any other message is processed.

## Web APIs

These may be [Browser APIs](https://developer.mozilla.org/en-US/docs/Web/API) or third-party APIs / libraries. **Browser APIs** are JavaScript code built into the browser, such as fetch, the DOM, Screen Capture, Drag & Drop. **Third-party APIs** are usually endpoints which need a connection made to them, such as a JSON/REST API. **Third-party libraries** are available to download and use with JavaScript and provide functionality beyond that of the Browser API.

## Behaviour

### Asynchronous Effect

JS is single-threaded and synchronous. To achieve asynchronicity, callbacks (or promises) are used. When making external API calls with fetch, ajax, axios, etc. other code doesn't get blocked because the request happens in the background, while the function call (e.g. `axios.get(url)`) stops. Only when the response has been fulfilled will the callback / promise be put into the message queue, where it waits it's turn to be called in the event loop.

An HTTP request is an OS feature and therefore JavaScript can command this to run in the background while the event loop resumes.

![Asynchronous API calls](./asynchronous%20js.drawio.png)

### setTimeout

The second argument in `setTimeout` indicates the _minimum_ delay which the function is called after. This is because if there are already messages in the message queue, it will have to wait for those messages to be fulfilled first. If there is no messages waiting in the message queue, it will be processed straight after the delay _(500ms)_. For this reason, large applications with lots of messages queued will perform callbacks slower.

```js
setTimeout(function () {}, 500)
```

### Multiple Runtimes

Part of why browsers such as Chrome or Firefox can be so memory heavy are because they use separate processes for each tab. This allows each tab to have it's own JS instance running. Separate runtimes such as WebWorkers and iframes can use `postMessage` and `window.onmessage` to send/receive messages from other JavaScript processes.

#### `<iframe>`

Frames are essentially embedded documents with their own JavaScript context. An `<iframe>` (inline frame) is an HTML element which embeds a separate HTML document. The iframe will have it's own JS context, but does not constitute as a separate runtime. This means iframes with scripts can block their parent document. To test this I've created a document, `parent.html` which has an iframe referencing `nested.html`.

`nested.html` contains a event listener which blocks the message queue for 1 second when called.

```html
<button id="blocker">Block</button>

<script>
	document.getElementById('blocker').addEventListener('click', () => {
		const start = Date.now()
		while (start + 1000 > Date.now()) {}
	})
</script>
```

When clicking the Block button you can see the counter in `parent.html` stop. It stops for exactly 1 second which is how long we wait for in the click event while loop.

##### Cross-origin iframes

Work slightly different to same-origin iframes in some browsers. Chrome, Opera and Microsoft Edge, for instance, does not get blocked when the same test is performed using the above code, while Firefox does get blocked by the iframe. This suggests it delegates a separate process for a cross-origin iframe element. You can test this yourself using the commented iframe in parent.html

[Out-of-Process iframes](https://www.chromium.org/developers/design-documents/oop-iframes) are documented by The Chromium Projects and are listed as a security measure.

#### WebWorkers

Are ways of running scripts in a background thread. They have all functionality of a normal JavaScript instance. Once created, they can send messages to the code that created it, via `postMessage`

To create a worker all you need is the path to a file containing JavaScript.

```js
const worker = new Worker('worker.js', {
	type: 'classic',
	credential: 'omit',
	name: 'MyWorker',
})
```

---

## References

- [What is a Memory Heap?](https://stackoverflow.com/questions/2308751/what-is-a-memory-heap)
- [Cpp Reference - malloc](http://www.cplusplus.com/reference/cstdlib/malloc/)
- [MDN - Web APIs](https://developer.mozilla.org/en-US/docs/Web/API)
- [MDN - Concurrency model and the event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)
- [MDN - iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
- [OOPIFs](https://www.chromium.org/developers/design-documents/oop-iframes) -[MDN - Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
