import { useEffect, useRef } from 'react'

/**
 * The custom hook useIsComponentMountedRef helps cancel async work
 * (like API requests) in unmounted components without repeating
 * boilerplate isMounted logic everywhere.
 *
 * @Returns a ref object whose `.current` value is true when the
 * component is mounted, and false after it unmounts.
 */
export default function useIsComponentMountedRef() {
  const isMountedRef = useRef(false)

  useEffect(() => {
    isMountedRef.current = true
    return () => {
      isMountedRef.current = false
    }
  }, [])

  return isMountedRef
}
