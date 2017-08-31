'use strict'

let botkit = require('botkit');
let os = require('os');
let fs = require('fs');
let util = require('util');

var controller = botkit.slackbot({
    debug: false
});

if (!process.env.token) {
    console.log('Error: Specify token in environment');
    process.exit(1);
}

//noinspection JSUnresolvedFunction
let gBot = controller.spawn({
    token: process.env.token
});

//gBot.startRTM(function (err) {
//    if (err) {
//        //noinspection JSClosureCompilerSyntax
//        throw new Error(err);
//    }
//});

module.exports = (content, callback) => {
    //console.log("Slackin: " + content);
    let req = JSON.parse(content);
    let res = {
      "slackit" : "v1",
      "request" : req
  };
    gBot.say({text: JSON.stringify(res), channel: "#blog"});
    callback(null, JSON.stringify(res));
};
