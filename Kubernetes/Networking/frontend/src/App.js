import React, { useState, useEffect, useCallback } from 'react';

import './App.css';
import TaskList from './components/TaskList';
import NewTask from './components/NewTask';

function App() {
  const [tasks, setTasks] = useState([]);

  const fetchTasks = useCallback(function () {
    // IP of the Tasks Server - HARDCODED - NOT GOOD
    // fetch('http://192.168.99.100:32140/tasks', {

    // Instead, let NGINX handle it. (see nginx.config file)
    // all requests that start with /api/* will be forwarded to another address 
    fetch('/api/tasks', {
      headers: {
        'Authorization': 'Bearer abc'
      }
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (jsonData) {
        setTasks(jsonData.tasks);
      });
  }, []);

  useEffect(
    function () {
      fetchTasks();
    },
    [fetchTasks]
  );

  function addTaskHandler(task) {
    // IP of the Tasks Server - HARDCODED - NOT GOOD
    // fetch('http://192.168.99.100:32140/tasks', {

    // Instead, let NGINX handle it. (see nginx.config file)
    // all requests that start with /api/* will be forwarded to another address 
    fetch('/api/tasks', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer abc',
      },
      body: JSON.stringify(task),
    })
      .then(function (response) {
        console.log(response);
        return response.json();
      })
      .then(function (resData) {
        console.log(resData);
      });
  }

  return (
    <div className='App'>
      <section>
        <NewTask onAddTask={addTaskHandler} />
      </section>
      <section>
        <button onClick={fetchTasks}>Fetch Tasks</button>
        <TaskList tasks={tasks} />
      </section>
    </div>
  );
}

export default App;
