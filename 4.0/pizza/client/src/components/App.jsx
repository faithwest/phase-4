import React from 'react';
import { BrowserRouter, Router, Routes , Route} from 'react-router-dom';
import PizzasList from './PizzasList';
import RestaurantsList from './RestaurantsList';

import pizza from './Pizza';
import RestaurantDescription from "./RestaurantDescription";


function App() {
  return (
    <div>
    <BrowserRouter>
  <Routes>
    <Router>

    <Route exact path="/restaurants/:id" components={<RestaurantDescription />} />
    <Route path="/" components ={RestaurantsList} />
    <Route path="/pizza" components={pizza} />
    <Route path="/pizzas" components={PizzasList} />
      
    </Router>
    </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
