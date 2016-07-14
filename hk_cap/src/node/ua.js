/**
 * Created by wuyue on 16/6/28.
 */

var userAgent = require('/usr/local/lib/node_modules/useragent.js');

var data = process.argv[2];

var ua = userAgent.analyze(data);

console.log(ua);