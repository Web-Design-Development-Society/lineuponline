import { useState, useEffect } from 'react'
import Timer from './Timer'

type Period = 'Focus' | 'Long Break' | 'Short Break'
export default function Pomodoro() {
  const [cyclesCompleted, setCyclesCompleted] = useState<number>(0)
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [currentPeriod, setCurrentPeriod] = useState<Period>('Focus')

  useEffect(() => {
    setCyclesCompleted(1)
  }, [])
  return (
    <>
      <h1>Pomodoro</h1>
      <section id="timer-section">
        <p>Cycles Completed: {cyclesCompleted}</p>
        <Timer />
      </section>
    </>
  )
}
