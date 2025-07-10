import React, { useState } from 'react'
import { CountdownCircleTimer } from 'react-countdown-circle-timer'

export default function Timer() {
  const [playing, setPlaying] = useState(false)
  const [timerLength, setTimerLength] = useState(25)

  const handleStart = () => {
    setPlaying(true)
  }

  const handleStop = () => {
    setPlaying(false)
  }

  const setCycle25 = () => {
    setTimerLength(25)
  }

  const setCycle45 = () => {
    setTimerLength(45)
  }

  return (
    <>
      <button onClick={setCycle25} className="time-btn">
        25
      </button>
      <button onClick={setCycle45} className="time-btn">
        45
      </button>
      <CountdownCircleTimer
        isPlaying={playing}
        duration={timerLength * 60}
        colors={['#004777', '#F7B801', '#A30000', '#A30000']}
        colorsTime={[7, 5, 2, 0]}
      >
        {(renderProps) => <FormatDisplay {...renderProps} />}
      </CountdownCircleTimer>
      <div>
        <button onClick={handleStart}>Start</button>
        <button onClick={handleStop}>Stop</button>
      </div>
    </>
  )
}

const FormatDisplay = ({ remainingTime }: { remainingTime: number }) => {
  const minutes = Math.floor(remainingTime / 60)
  const seconds = remainingTime % 60
  return (
    <p>
      {minutes}:{seconds.toString().padStart(2, '0')}
    </p>
  )
}
