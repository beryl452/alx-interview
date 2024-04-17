#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

const options = {
  url: '',
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (_err, _res, _body) => {
          if (_err) {
            reject(_err);
          }
          resolve(JSON.parse(_body).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.log(err));
  } else {
    console.log(error);
  }
}

if (process.argv.length > 2) {
  options.url = `${API_URL}/films/${process.argv[2]}/`;
  request.get(options, callback);
}
