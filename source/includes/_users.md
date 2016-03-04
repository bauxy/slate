# Users
`users/` endpoint: login accounts to our system.

Users can be individuals who have signed up with us, in which case they are tied to a single Patient account. Alternately, they may be healthcare providers, who manage a number of Patient accounts.
<aside class="warning">
TODO: is users/ even exposed to the outside world yet? What’s the interface?
</aside>

<aside class="notice">
Note that one creates a user by <code>POST</code>ing to <code>patients/</code> or
<code>providers/</code>; <code>POST users/</code> is forbidden. This is because
every user must fall into one of those two classes.
</aside>
