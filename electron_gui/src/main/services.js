import exampleService from "./services/example";

export var services=[
    exampleService
]

export function makeChannelName(name, fnName) {
    return `${name}.${fnName}`;
}