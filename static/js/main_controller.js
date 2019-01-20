var app = angular.module('elections-app', []);

app.controller("main-controller", function ($scope, $http) {
    $http.get('/getProvinces').success(function(response) {
      // var response = JSON.parse(response);
      console.log(response);
    }).error(function(response) {
      console.log(response);
    });
});
