import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PizzasList = () => {
  const [pizzas, setPizzas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = () => {
      axios.get('http://127.0.0.1:5555/pizzas')
        .then(response => {
          setPizzas(response.data);
        })
        .catch(error => {
          setError(error.message);
        })
        .finally(() => {
          setLoading(false);
        });
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>Pizzas List</h2>
      {loading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
      {pizzas.length > 0 && (
        <ul>
          {pizzas.map((pizza) => (
            <li key={pizza.id}>
              <strong>{pizza.name}{pizza.price}{pizza.restaurant}</strong> - {pizza.ingredients}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default PizzasList;
