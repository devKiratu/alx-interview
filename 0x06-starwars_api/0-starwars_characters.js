#!/usr/bin/node

const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length >= 3) {
  const movieId = parseInt(process.argv[2]);
  const url = `${baseUrl}/films/${movieId}`;

  request(url, (err, res, body) => {
    if (err) {
      process.exit(1);
    }
    const data = JSON.parse(body);
    const characters = data.characters;
    if (characters) {
      const promises = characters.map((item) => {
        return new Promise((resolve, reject) => {
          request(item, (err, res, body) => {
            const data = JSON.parse(body);
            resolve(data.name);
            reject(err);
          });
        });
      });
      Promise.all(promises)
        .then(values => {
          values.forEach((value) => console.log(value));
        });
    }
  });
}
