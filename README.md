🚀 Boom Action JS

Automate Boom Token interactions,liquidity management, and analytics using GitHub Actions.

[![Lint Codebase](https://github.com/Boomtoknlab/boom-action-js/actions/workflows/lint.yml/badge.svg)](https://github.com/Boomtoknlab/boom-action-js/actions)  
[![Continuous Integration](https://github.com/Boomtoknlab/boom-action-js/actions/workflows/ci.yml/badge.svg)](https://github.com/Boomtoknlab/boom-action-js/actions)  

🌟 Features

✅ Automated Smart Contract Transactions – Execute BOOM transfers, liquidity adjustments, and staking.
✅ Real-Time On-Chain Analytics – Fetch price, liquidity, and trading volume data.
✅ Multi-Chain Support – Works with Base, BSC, and Ethereum.
✅ Secure Execution – Uses GitHub Secrets for private key handling.
✅ Easy CI/CD Integration – Automate blockchain operations directly in GitHub workflows.

📦 Installation & Usage

⚙️ Inputs
Name	Description	Required
private-key	Private key for transactions	✅ Yes
rpc-url	RPC URL of the blockchain	✅ Yes

🔍 Outputs
Name	Description
result	Output result of the executed action

🛠 Development & Setup
	1.	Clone the repository:
 git clone https://github.com/Boomtoknlab/boom-action-js.git
cd boom-action-js

2.	Install dependencies:
npm install

	3.	Build the project:
npm run build

	4.	Test the action locally:
 npm test

🔄 Versioning & Publishing
To release a new version:
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0

📜 License

MIT License © 2025 Boomtoknlab
