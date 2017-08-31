'use strict'

const RxHttpRequest = require('rx-http-request').RxHttpRequest;
var Rx = require('rxjs/Rx');

function down_notifier(url) {
  return RxHttpRequest.post('http://gateway:8080/function/url_ping', {
      body : {
        url: url
      },
      json: true
    })
    .map(r => r.body)
    .map(r => {
      //console.log("parsed json from url_ping: " + r.status);
      if(r.status !== "ok") {
        return RxHttpRequest.post('http://gateway:8080/function/slack_it', {
            body: r,
            json: true
        })
        .map(r => r.body);
        //return "ping failed - told slack";
      } else {
        return Rx.Observable.of("all ok - slack not informed");
      }
    });
}

module.exports = (content, callback) => {
    //console.log("Slackin: " + content);
    let req = JSON.parse(content);

    down_notifier(req.url).subscribe(
        (x) => {
          x.subscribe(r => {
            let res = {
              "DownNotifier" : "v1",
              "request" : req,
              "response": r
            };

            callback(null, JSON.stringify(res));
          });
        },
        (err) => {
            console.log('Error: ' + err);
        },
        () => {
            //console.log('Completed');
        });
};
