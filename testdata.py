abi = {
  "version": "1.0",
  "contract_account": "",
  "functions": [
    {
      "name": "deposit",
      "inputs": [
        {
          "name": "user",
          "type": "account"
        },
        {
          "name": "amount",
          "type": "uint64"
        }
      ],
      "outputs": [
        {
          "name": "returnValue0",
          "type": "bool"
        }
      ]
    },
    {
      "name": "deposit_msg",
      "inputs": [
        {
          "name": "transfer_msg",
          "type": "TransferReceipts[]",
          "components": []
        }
      ],
      "outputs": [
        {
          "name": "returnValue0",
          "type": "string"
        }
      ]
    },
    {
      "name": "withdraw",
      "inputs": [
        {
          "name": "user",
          "type": "account"
        },
        {
          "name": "amount",
          "type": "uint64"
        }
      ],
      "outputs": [
        {
          "name": "returnValue0",
          "type": "bool"
        }
      ]
    }
  ],
  "events": [
    {
      "name": "Deposit",
      "inputs": [
        {
          "name": "from",
          "type": "account"
        },
        {
          "name": "to",
          "type": "account"
        },
        {
          "name": "amount",
          "type": "uint64"
        }
      ]
    },
    {
      "name": "Withdraw",
      "inputs": [
        {
          "name": "from",
          "type": "account"
        },
        {
          "name": "to",
          "type": "account"
        },
        {
          "name": "amount",
          "type": "uint64"
        }
      ]
    }
  ]
}

components = [
  {
    "name": "Transfer",
    "type": "struct",
    "components": [
      {
        "name": "from",
        "type": "account"
      },
      {
        "name": "to",
        "type": "account"
      },
      {
        "name": "amount",
        "type": "uint64"
      }
    ]
  },
  {
    "name": "TransferReceipts",
    "type": "struct",
    "components": [
      {
        "name": "trans",
        "type": "Transfer[]",
        "components": []
      },
      {
        "name": "message",
        "type": "string"
      }
    ]
  }
]