import React from 'react'
import { CountdownCircleTimer } from 'react-countdown-circle-timer'

export default function Timer() {
  return (
    <>
      <CountdownCircleTimer
        isPlaying
        duration={15 * 60}
        colors={['#004777', '#F7B801', '#A30000', '#A30000']}
        colorsTime={[7, 5, 2, 0]}
      >
        {(renderProps) => <FormatDisplay {...renderProps} />}
      </CountdownCircleTimer>
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
