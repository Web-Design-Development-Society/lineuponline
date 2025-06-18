import { useEffect, useState } from 'react'

/* eslint-disable */
interface CompletedCycles {
  [date: string]: Cycle[]
}

interface Cycle {
  id: string
  name: string
  stateTime: Date
  duration: number
}

interface TimerProgress {
  // cycle: Cycle
  totalMs: number
  currentMs: number
  paused: boolean
}

export default function FakeTimerState() {
  const [cycles, setCycles] = useState<Cycle[]>([])

  useEffect(() => {
    console.log('This logged right after the component rendered')
  }, [])

  useEffect(() => {
    console.log('This logs every time cycles changes')
  }, [cycles])

  return (
    <>
      <p>State: </p>
      <button></button>
    </>
  )
}
