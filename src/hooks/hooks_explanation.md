# Hooks Folder

Custom React hooks live here.

Hooks are reusable functions that start with `use` (e.g. `useFetch`, `useAuth`). They let you encapsulate logic you want to share between components.

Example:

```jsx
// useCounter.js
import { useState } from 'react'

export function useCounter() {
  const [count, setCount] = useState(0)
  const increment = () => setCount((c) => c + 1)
  return { count, increment }
}
```

Some built in react hooks are

- useState
- useEffect
- useReducer
- useCallback
- useMemo
