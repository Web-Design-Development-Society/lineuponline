export default {
  '*.{js,ts,jsx,tsx}': (stagedFiles) => [
    `prettier --write ${stagedFiles.join(' ')}`,
    `eslint --fix --max-warnings=0 ${stagedFiles.join(' ')}`
  ]
}
