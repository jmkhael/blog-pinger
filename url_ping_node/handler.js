'use strict'

const RxHttpRequest = require('rx-http-request').RxHttpRequest;
var Rx = require('rxjs/Rx');

function url_ping(url) {
  return RxHttpRequest.get(url, {
      timeout: 20000,
      json: true
    })
    .map(r => {
      let statusCode = r.response.statusCode;
      //console.log("parsed json from url_ping: " + statusCode);
      if(statusCode !== 200) {
        return Rx.Observable.of({
          "url": url,
          "status":"nok",
          "status_code": statusCode,
          "error": r.body
        });
      } else {
        //return Rx.Observable.of("all ok - slack not informed");
        return Rx.Observable.of({
          "url": url,
          "status":"ok",
          "status_code": statusCode
        });
      }
    });
}

module.exports = (content, callback) => {
    //console.log("Slackin: " + content);
    let req = JSON.parse(content);
    let url = req.url;

    url_ping(url).subscribe(
        (x) => {
          x.subscribe(r => {
            callback(null, JSON.stringify(r));
          });
        },
        (err) => {
            //console.log('Error: ' + err);
            let r = {
              "url": url,
              "status":"nok",
              "error": err
            };
            callback(null, JSON.stringify(r));
        },
        () => {
            //console.log('Completed');
        });
};
