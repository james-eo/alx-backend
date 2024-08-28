# 0x03. Queuing System in JS

## Project Overview
This project focuses on creating a queuing system using JavaScript, Redis, Node.js, ExpressJS, and Kue. The goal is to gain a deep understanding of how to manage queues in a backend system, leveraging Redis for data persistence and real-time operations.

## Resources
- [Redis Quick Start](https://redis.io/topics/quickstart)
- [Redis Client Interface](https://redis.io/clients)
- [Redis Client for Node.js](https://github.com/NodeRedis/node-redis)
- [Kue (Deprecated)](https://github.com/Automattic/kue)

## Learning Objectives
By the end of this project, you should be able to explain and demonstrate the following:

- How to run a Redis server on your machine.
- How to perform simple operations with the Redis client.
- How to use a Redis client with Node.js for basic operations.
- How to store hash values in Redis.
- How to handle asynchronous operations with Redis.
- How to use Kue as a queue system.
- How to build a basic Express app interacting with a Redis server.
- How to build an Express app that interacts with both a Redis server and a queue.

## Requirements
- **Environment:** Ubuntu 18.04, Node 12.x, Redis 5.0.7
- **Coding Style:** All files should end with a new line. Code should use the `.js` extension.
- **Mandatory Files:** A `README.md` file at the root of the project.

## Setup Instructions

1. **Install Redis Instance**
   - Download, extract, and compile the latest stable Redis version (higher than 5.0.7).
   - Start Redis in the background.
   - Set and retrieve values using the Redis client.

    ```bash
    $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
    $ tar xzf redis-6.0.10.tar.gz
    $ cd redis-6.0.10
    $ make
    $ src/redis-server &
    $ src/redis-cli ping
    PONG
    $ src/redis-cli set Holberton School
    OK
    $ src/redis-cli get Holberton
    "School"
    $ kill [PID_OF_Redis_Server]
    ```

2. **Node Redis Client**
   - Install `node_redis` using npm.
   - Create a script `0-redis_client.js` to connect to the Redis server and handle connection status.

3. **Basic Redis Operations**
   - Create `1-redis_op.js` to set and get values in Redis using callbacks.

4. **Async Redis Operations**
   - Modify the previous code to create `2-redis_op_async.js` and use `async/await` for Redis operations.

5. **Advanced Redis Operations**
   - Create `4-redis_advanced_op.js` to store and retrieve hash values using Redis.

6. **Redis Client Publisher and Subscriber**
   - Implement a basic publisher and subscriber in Redis using `5-subscriber.js` and `5-publisher.js`.

7. **Job Creation**
   - Create a job creator using Kue in `6-job_creator.js`.

## Required Files for the Project
- `package.json`
- `.babelrc`

Ensure to run `$ npm install` after setting up the `package.json`.

## Tasks

### 0. Install a Redis Instance
- Set up Redis and confirm that it's running correctly on your machine.

### 1. Node Redis Client
- Install and configure `node_redis`.
- Create a connection script that logs connection status.

### 2. Node Redis Client and Basic Operations
- Implement basic Redis operations using callbacks.

### 3. Node Redis Client and Async Operations
- Modify the basic operations to use `async/await`.

### 4. Node Redis Client and Advanced Operations
- Store and retrieve hash values in Redis.

### 5. Node Redis Client Publisher and Subscriber
- Implement a Redis publisher and subscriber to handle messages.

### 6. Job Creator
- Create a job queue with Kue and add jobs to it.
