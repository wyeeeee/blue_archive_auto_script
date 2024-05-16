import exampleService from "./services/example";
import configService from "./services/config";
export var services=[
    exampleService,
    configService
]

export function makeChannelName(name, fnName) {
    return `${name}.${fnName}`;
}