**Your Quest: Become a Go Backend Virtuoso!**

**Instructions:**

1.  **Follow Sequentially:** Each level builds upon the previous one.
2.  **Code Actively:** Don't just read; write the code, run it, debug it. Understanding comes from doing.
3.  **Research:** If a concept is new, take time to read Go documentation (`godoc net/http`, etc.) or search for tutorials/articles on that specific topic.
4.  **Experiment:** Modify the code, try different approaches. How does changing X affect Y?
5.  **Focus on _Why_:** Understand _why_ we use certain patterns (like interfaces, context, channels).

---

**Level 1: The Humble HTTP Server (Foundation: `net/http`)**

- **Goal:** Understand the absolute basics of handling web requests in Go without frameworks.

1.  **Theory:** What is HTTP? Explain the difference between a GET and a POST request in your own words. What is an HTTP status code (give examples like 200, 404, 500)?
2.  **Task 1 (Basic Handler):** Write a simple Go program using `net/http` that starts a web server on port `8080`. Create a handler function for the root path (`/`) that responds with the plain text "Welcome to the Go Backend Quest!". Use `http.HandleFunc` and `http.ListenAndServe`.
3.  **Task 2 (Multiple Routes):** Modify your server to handle two routes:
    - `/greet`: Responds with "Hello, Adventurer!"
    - `/farewell`: Responds with "Goodbye for now!"
4.  **Task 3 (Reading Request Info):** Modify the `/greet` handler. Check if there's a URL query parameter named `name` (e.g., `/greet?name=Budi`). If present, respond with "Hello, [Name]!"; otherwise, stick to "Hello, Adventurer!". (Hint: Use `r.URL.Query().Get("name")`).
5.  **Task 4 (Different Methods):** Create a new handler for `/submit`.
    - If the request method is GET, respond with "Please submit data using POST." (Hint: Use `r.Method`).
    - If the request method is POST, respond with "Data submitted successfully!" (You don't need to process data yet).
    - For any other method, respond with a `405 Method Not Allowed` status code. (Hint: `w.WriteHeader(http.StatusMethodNotAllowed)`).

**Checkpoint 1:** You can now create basic HTTP servers, handle different routes and methods, and read simple query parameters using Go's standard library.

---

**Level 2: Speaking JSON & Structuring Data (APIs Begin)**

- **Goal:** Learn to handle JSON data, a cornerstone of modern APIs, and structure your data using structs.

1.  **Theory:** What is JSON? Why is it commonly used for APIs? What are Go's `encoding/json` package's `Marshal` and `Unmarshal` functions used for?
2.  **Task 1 (Struct Definition):** Define a Go struct named `Task` with the following fields:
    - `ID` (int, use JSON tag `json:"id"`)
    - `Title` (string, use JSON tag `json:"title"`)
    - `Completed` (bool, use JSON tag `json:"completed"`)
3.  **Task 2 (Returning JSON):** Create a handler for `/tasks` (GET method). Inside the handler, create a _slice_ of `Task` structs with some sample data. Use `json.NewEncoder(w).Encode()` to marshal this slice into JSON and send it as the response. Don't forget to set the `Content-Type` header to `application/json` (`w.Header().Set("Content-Type", "application/json")`).
4.  **Task 3 (Receiving JSON):** Create a handler for `/tasks` (POST method).
    - This handler should expect a JSON payload in the request body representing a _single_ new `Task` (without an ID, perhaps).
    - Use `json.NewDecoder(r.Body).Decode()` to unmarshal the JSON into a `Task` struct variable.
    - For now, just print the received task's `Title` to the _server's console_ using `fmt.Println`.
    - Respond with a success message (e.g., JSON `{"message": "Task received"}`) and status `201 Created`.
    - **Bonus:** Add basic error handling if the JSON decoding fails (respond with `400 Bad Request`).
5.  **Task 4 (Simple In-Memory Store):** Modify your server:
    - Create a global variable (or use closures if you prefer) to hold a slice of `Task` structs (our "database" for now).
    - Modify the GET `/tasks` handler to return the tasks from this global slice.
    - Modify the POST `/tasks` handler:
      - Decode the incoming task.
      - Assign it a unique ID (e.g., just increment a counter).
      - Append the new task to the global slice.
      - Return the _newly created task_ (including its assigned ID) as JSON in the response.

**Checkpoint 2:** You can define data structures, send JSON responses, receive and parse JSON request bodies, and manage simple in-memory data for your API.

---

**Level 3: Go's Superpower - Concurrency (Goroutines & Channels)**

- **Goal:** Understand and utilize Go's lightweight concurrency primitives.

1.  **Theory:** What is a goroutine? How is it different from a traditional OS thread? What is a channel? What are channels used for (communication, synchronization)? Explain the difference between buffered and unbuffered channels.
2.  **Task 1 (Simple Goroutine):** Write a program where the `main` function launches a goroutine that prints "Processing in background..." after a 2-second delay (`time.Sleep`). The `main` function should print "Main function continues..." immediately and then wait for 3 seconds before exiting (to allow the goroutine time to finish). Why is the final wait necessary here?
3.  **Task 2 (Using Channels for Results):** Modify Task 1. Instead of just printing, the goroutine should perform a mock "calculation" (e.g., `time.Sleep(2 * time.Second); result := 42`). It should send this result back to the `main` function via a channel. The `main` function should wait to _receive_ the result from the channel and then print "Calculation result: [result]".
4.  **Task 3 (Applying to Backend - Mock Processing):** Let's simulate processing a task asynchronously.
    - Modify your POST `/tasks` handler from Level 2.
    - When a new task is received:
      - Immediately respond to the client with `202 Accepted` and a message like `{"message": "Task accepted for processing"}`.
      - Launch a _goroutine_ to handle the "heavy processing" (simulated by a `time.Sleep(5 * time.Second)`).
      - Inside the goroutine, after the sleep, print "Processed task: [Task Title]" to the _server console_.
    - **Discussion:** What are the pros and cons of this "fire-and-forget" approach? When might it be suitable/unsuitable?
5.  **Task 4 (Worker Pool Pattern - Basic):** Imagine needing to process many tasks concurrently but limiting the number of simultaneous operations.
    - Create a buffered channel (e.g., `jobs := make(chan Task, 10)`).
    - Create another channel for results (e.g., `results := make(chan string)`).
    - Start 3 "worker" goroutines. Each worker loops forever, reading a `Task` from the `jobs` channel, simulating work (`time.Sleep`), and sending a completion message (e.g., "Worker [id] finished job [Task Title]") to the `results` channel.
    - In your `main` (or a relevant function), send 5 sample `Task`s into the `jobs` channel.
    - Read 5 results from the `results` channel and print them.
    - **Concept:** How does the buffered `jobs` channel help manage the flow? How does this pattern limit concurrency?

**Checkpoint 3:** You can now launch concurrent operations using goroutines and coordinate them or pass data using channels. You understand the basics of asynchronous processing and worker pools.

---

**Level 4: Talking to Databases (Persistence)**

- **Goal:** Learn how to connect to and interact with a relational database (like PostgreSQL or MySQL) using Go.

1.  **Setup:** Install PostgreSQL (or MySQL/SQLite). Create a database and a table named `tasks` that matches the `Task` struct (columns: `id SERIAL PRIMARY KEY`, `title VARCHAR(255)`, `completed BOOLEAN`).
2.  **Theory:** What is SQL? What are the basic CRUD operations in SQL (SELECT, INSERT, UPDATE, DELETE)? What is the purpose of Go's `database/sql` package? What is a database driver and why do you need one (e.g., `pq` for PostgreSQL, `go-sql-driver/mysql`)? What is SQL Injection and why is using prepared statements (`db.Prepare`, `db.QueryRow`, `stmt.Exec`) important?
3.  **Task 1 (Connection & Ping):** Write Go code to:
    - Import `database/sql` and the appropriate driver (`_ "github.com/lib/pq"` or similar).
    - Construct the database connection string (DSN). Consider using environment variables for credentials!
    - Open a database connection using `sql.Open`.
    - Ping the database using `db.Ping()` to verify the connection. Handle potential errors.
    - Use `defer db.Close()` to ensure the connection is closed.
4.  **Task 2 (Inserting Data):** Modify your POST `/tasks` handler:
    - Instead of appending to the in-memory slice, use `db.Exec()` or `db.Prepare()` followed by `stmt.Exec()` to execute an SQL `INSERT` statement to add the new task to the `tasks` table. Remember to use placeholders (`$1`, `$2` for pq; `?`, `?` for mysql) to prevent SQL injection!
    - Retrieve the ID of the newly inserted row (databases often support a `RETURNING id` clause or similar; research this for your chosen DB/driver). Update the `Task` struct with the ID.
    - Return the complete `Task` (with DB ID) as JSON.
5.  **Task 3 (Querying Data):** Modify your GET `/tasks` handler:
    - Use `db.Query()` to execute a `SELECT * FROM tasks` statement. Handle errors.
    - Use `defer rows.Close()`.
    - Iterate through the results using `rows.Next()`.
    - For each row, use `rows.Scan()` to scan the column values into the fields of a `Task` struct variable.
    - Append each scanned `Task` to a slice.
    - Marshal and return the slice as JSON.
6.  **Task 4 (Querying Single Item & Updating):**
    - Create a handler for GET `/tasks/{id}` (you'll need a router that supports path parameters later, or parse `r.URL.Path` for now). Use `db.QueryRow()` to fetch a single task by its ID. Handle the `sql.ErrNoRows` error specifically (return 404). Return the task as JSON.
    - Create a handler for PUT `/tasks/{id}`. It should receive task data (title, completed) as JSON. Use `db.Exec()` with an `UPDATE` statement and placeholders to update the task with the given ID in the database. Return the updated task or a success message.
7.  **Task 5 (Deleting):** Create a handler for DELETE `/tasks/{id}`. Use `db.Exec()` with a `DELETE` statement and a placeholder for the ID. Return a `204 No Content` status on success.

**Checkpoint 4:** You can connect to a SQL database, perform CRUD operations safely using prepared statements, and handle results, including potential errors like `sql.ErrNoRows`.

---

**Level 5: Frameworks & Structure (Building Smarter)**

- **Goal:** Utilize a web framework (like Gin or Echo) to simplify routing, request binding, and middleware, and structure your project logically.

1.  **Theory:** Why use a web framework? What benefits do they provide over plain `net/http` (e.g., routing, middleware, request binding, validation)? What is middleware in the context of web frameworks?
2.  **Setup:** Choose a framework (Gin is popular: `go get -u github.com/gin-gonic/gin`).
3.  **Task 1 (Basic Setup & Routing):** Refactor your Level 4 application using Gin (or your chosen framework):
    - Create a new Gin engine (`router := gin.Default()`).
    - Define your routes (GET `/tasks`, POST `/tasks`, GET `/tasks/:id`, PUT `/tasks/:id`, DELETE `/tasks/:id`) using the framework's methods (e.g., `router.GET`, `router.POST`, etc.). Notice how path parameters like `:id` are handled.
    - Adapt your existing handler functions to the framework's handler signature (e.g., `func(c *gin.Context)`). Access request data (body, params, query) using the framework's context object (e.g., `c.Param("id")`, `c.ShouldBindJSON(&task)`).
    - Send responses using the framework's helpers (e.g., `c.JSON(http.StatusOK, tasks)`).
    - Start the server using `router.Run(":8080")`.
4.  **Task 2 (Request Binding & Validation):**
    - Modify your `Task` struct using framework-specific tags for validation (e.g., Gin's `binding:"required"`).
    - In your POST and PUT handlers, use the framework's binding capabilities (e.g., `c.ShouldBindJSON(&task)`) to automatically parse the request body into your struct _and_ perform validation.
    - If binding/validation fails, the framework often helps return a 400 error. Handle this gracefully.
5.  **Task 3 (Middleware - Logging):** Most frameworks come with default middleware (like a logger and recovery). Gin's `gin.Default()` includes these. Observe the logs generated. Write a simple _custom_ middleware function that prints the HTTP method and path for every request _before_ it hits the handler. Register this middleware globally using `router.Use()`.
6.  **Task 4 (Project Structure):** Organize your code. Don't put everything in `main.go`. Create separate packages/directories:
    - `cmd/server/main.go`: Main application entry point, sets up router, starts server.
    - `internal/handlers` (or `pkg/handlers`): Contains your HTTP handler functions (`TaskHandler` struct with methods?).
    - `internal/models` (or `pkg/models`): Contains your `Task` struct definition.
    - `internal/store` (or `pkg/store`): Code related to database interaction (your `db.Query`, `db.Exec` logic). Define a `Store` interface and implementation.
    - **Dependency Injection:** How would you make the database connection (`*sql.DB`) available to your handlers/store? (Pass it during setup).

**Checkpoint 5:** You can leverage a web framework for cleaner routing, easier request handling/validation, and middleware. You understand the importance of organizing code into logical packages.

---

**Level 6: Interfaces, Testing & Robust Errors (Maintainability)**

- **Goal:** Write more flexible, testable, and robust code using interfaces, unit tests, and better error handling.

1.  **Theory:** What is an interface in Go? How does it promote decoupling? Why is decoupling important for testing and maintainability? What is unit testing? What is table-driven testing in Go?
2.  **Task 1 (Store Interface):** Define a `TaskStore` interface in your `store` package. It should declare methods matching your database operations (e.g., `GetAll() ([]models.Task, error)`, `Create(task *models.Task) error`, `GetByID(id int) (*models.Task, error)`, etc.). Make your database implementation (`PostgresStore`?) satisfy this interface.
3.  **Task 2 (Dependency Injection with Interface):** Modify your handler setup (e.g., `TaskHandler` struct). Instead of holding a concrete `*PostgresStore`, it should hold a `TaskStore` interface type. Inject the concrete database store instance during handler creation in `main.go`. Why does this make the handler more flexible?
4.  **Task 3 (Unit Testing Handlers - Mocking):** Write unit tests for one of your _handlers_ (e.g., GET `/tasks`).
    - Create a _mock_ implementation of the `TaskStore` interface. This mock doesn't need a real database; it just returns predefined data or errors for testing purposes.
    - In your test function (`TestGetTasksHandler` in `handlers/handler_test.go`):
      - Instantiate your handler, injecting the _mock_ store.
      - Create a test HTTP request (`httptest.NewRequest`).
      - Create a response recorder (`httptest.NewRecorder`).
      - Serve the request using your framework's router (or directly call the handler function).
      - Assert the response status code (`rr.Code`) and the response body (`rr.Body.String()`, you might need to unmarshal JSON) are as expected.
    - Use table-driven tests to cover different scenarios (e.g., success, store returns error, store returns empty list).
5.  **Task 4 (Unit Testing Store):** Write unit tests for your _database store_ implementation. This is harder as it touches a real DB. Options:
    - Use a dedicated test database.
    - Use libraries that help manage test DB state (e.g., `testcontainers-go`).
    - (Simpler for now) Focus on testing the _logic_ within the store methods, perhaps by mocking the `*sql.DB` itself (more advanced mocking). _Start by testing simpler store logic if possible._
6.  **Task 5 (Custom Errors):** Define custom error types or variables (e.g., `var ErrTaskNotFound = errors.New("task not found")`). Have your `TaskStore` methods return these specific errors when appropriate (e.g., `GetByID` returns `ErrTaskNotFound` instead of generic `sql.ErrNoRows`). Modify your handlers to check for these specific errors using `errors.Is` or type assertions and return appropriate HTTP status codes (e.g., 404 for `ErrTaskNotFound`).

**Checkpoint 6:** You can design decoupled components using interfaces, inject dependencies, write unit tests with mocks, and implement more specific error handling for robust APIs.

---

**Level 7: Context, Advanced Middleware & Security (Production Readiness)**

- **Goal:** Understand request lifecycles using `context`, implement more complex middleware, and add basic security measures.

1.  **Theory:** What is `context.Context` used for in Go servers? How does it handle request cancellation, deadlines, and passing request-scoped values?
2.  **Task 1 (Context in Handlers):** Modify your `TaskStore` interface methods and implementations to accept `ctx context.Context` as the first argument (e.g., `GetAll(ctx context.Context) ([]models.Task, error)`). Pass the request's context (`c.Request.Context()`) down from your handlers to the store methods. Use `db.QueryContext`, `db.ExecContext`, etc., in your store implementation. Why is this important for handling timeouts or client disconnects?
3.  **Task 2 (Request-Scoped Values via Context):** Write middleware that extracts a hypothetical `X-User-ID` header from the request. If present, store this user ID _in the request's context_. Write another handler that retrieves this user ID from the context and prints it. (Research: `context.WithValue`, but be cautious about its use).
4.  **Task 3 (Authentication Middleware - Simple):** Write middleware that checks for a static API key in an `Authorization` header (e.g., `Authorization: Bearer YOUR_SECRET_KEY`). If the key is missing or invalid, the middleware should abort the request with a `401 Unauthorized` error (`c.AbortWithStatusJSON`). Apply this middleware to specific routes or groups that require protection.
5.  **Task 4 (Password Hashing):** Add a `User` model (`ID`, `Username`, `PasswordHash string`). Add a `/signup` endpoint. When a user signs up (provides username/password):
    - Use the `golang.org/x/crypto/bcrypt` package to generate a hash from the user's password (`bcrypt.GenerateFromPassword`).
    - Store the `Username` and the _hashed password_ in a new `users` table. **NEVER store plain text passwords.**
6.  **Task 5 (Login Endpoint):** Create a `/login` endpoint. It receives username/password.
    - Fetch the user record from the DB by username.
    - If the user exists, use `bcrypt.CompareHashAndPassword` to compare the stored hash with the provided password.
    - If they match, return a success message (later, you'd return a token like JWT). If not, return `401 Unauthorized`.

**Checkpoint 7:** You understand `context` for request lifecycle management, can implement custom middleware for logging, auth, etc., and know the basics of secure password handling.

---

**Level 8: Deployment & Optimization Basics (Beyond Code)**

- **Goal:** Get a taste of packaging your application for deployment and basic performance considerations.

1.  **Theory:** What is Docker? What is a container? What is a Dockerfile? Why is containerization useful for deployment? What is profiling?
2.  **Task 1 (Dockerfile):** Create a basic `Dockerfile` for your Go application.
    - Use a multi-stage build:
      - Stage 1: Use a Go base image (`golang:...-alpine`) to build your application (`go build -o /server ./cmd/server`).
      - Stage 2: Use a minimal base image (`alpine:latest`). Copy the compiled binary from Stage 1. Expose the port your server runs on (`EXPOSE 8080`). Set the command to run your binary (`CMD ["/server"]`).
    - Build the Docker image (`docker build -t go-backend-quest .`).
    - Run the container (`docker run -p 8080:8080 go-backend-quest`). Test if you can access your API.
3.  **Task 2 (Configuration):** Stop hardcoding things like the database DSN or API keys. Use environment variables or a configuration library (e.g., Viper) to manage these settings. Modify your code to read configuration at startup. Update your Dockerfile/`docker run` command to pass in environment variables.
4.  **Task 3 (Basic Benchmarking):** Use Go's built-in benchmarking tools. Write a simple benchmark test function (`func BenchmarkGetTasksHandler(b *testing.B)`) for your GET `/tasks` handler. Use the `testing` package and `httptest` similar to unit tests, but loop `b.N` times. Run it with `go test -bench=.`. (Note: Meaningful benchmarks require careful setup).
5.  **Task 4 (Profiling - Intro):** Learn how to enable Go's `net/http/pprof` endpoint. Add `import _ "net/http/pprof"` and register its handlers (often done on a separate port or path for security). Run your application and access the pprof UI (e.g., `http://localhost:6060/debug/pprof/`). Explore the different profiles available (heap, goroutine, CPU). _Actually interpreting profiles effectively is a deep skill, but knowing how to generate them is the first step._

**Final Checkpoint:** You have containerized your application using Docker, externalized configuration, and have been introduced to the basic tools for benchmarking and profiling Go applications.

---

**Congratulations, Adventurer!**

Completing this quest means you've covered a vast range of essential Go backend development skills, from basic HTTP handling to concurrency, databases, testing, security basics, and deployment concepts.

**"Maxed Out"?** Real-world development involves continuous learning, deeper dives into specific areas (advanced database optimization, specific cloud platform services, complex distributed systems, gRPC, GraphQL, different auth mechanisms like JWT/OAuth), and gaining experience through building and maintaining real applications.

However, you now have a **very strong foundation** and the practical skills required for many junior-to-mid-level Go backend roles. Keep building, keep learning, and stay curious!
