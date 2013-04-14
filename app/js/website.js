var Site = angular.module('Website', []);

Site.config(function ($routeProvider) {
  $routeProvider
    .when('/home',  {templateUrl: 'parts/home.html', controller: 'RouteController'})  
    .when('/who',   {templateUrl: 'parts/who.html', controller: 'RouteController'})
    .when('/what',  {templateUrl: 'parts/what.html', controller: 'RouteController'})
    .when('/where', {templateUrl: 'parts/where.html', controller: 'RouteController'})
    .otherwise({redirectTo: '/home'});
});

function AppController ($scope, $rootScope, $http) {
  // Load pages on startup
  $http.get('pages.json').success(function (data) {
    $rootScope.pages = data;
  });

  // Set the slug for menu active class
  $scope.$on('routeLoaded', function (event, args) {
    $scope.slug = args.slug;
  });
}

function RouteController ($scope, $rootScope, $routeParams) {
  // Getting the slug from $routeParams
  var slug = $routeParams.slug;
  
  $scope.$emit('routeLoaded', {slug: slug});
  $scope.page = $rootScope.pages[slug];
}