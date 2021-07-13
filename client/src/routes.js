import React from "react";
import { Route, Switch, BrowserRouter } from "react-router-dom";
import Dashboard from "./pages/Dashboard/index";
import Login from "./pages/Login/index";
import GlobalStateProvider from "./hooks/globalState";
export default function Routes() {
  return (
    <BrowserRouter>
      <GlobalStateProvider>
        <Switch>
          <Route exact path="/" component={Dashboard} />
          <Route exact path="/login" component={Login} />
        </Switch>
      </GlobalStateProvider>
    </BrowserRouter>
  );
}
