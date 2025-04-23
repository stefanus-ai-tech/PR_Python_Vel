package main

import (
	"net/http"
	"regexp"
)

type route struct {
	method  string
	pattern *regexp.Regexp
	innerHandler http.HandlerFunc
	paramKeys []string
}

type router struct {
	routes []route
}

func newRouter()*router {
	return &router{routes: []route{}}
}