import 'package:flutter/material.dart';

class Chat extends StatefulWidget {
  Chat({Key? key}) : super(key: key);

  @override
  State<Chat> createState() => _ChatState();
}

class _ChatState extends State<Chat> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 30, horizontal: 20),
            child: Row(
              children: [
                IconButton(
                  icon: const Icon(Icons.arrow_back),
                  onPressed: () {
                    Navigator.of(context).pop();
                  },
                ),
                const SizedBox(
                  width: 220,
                ),
                const Text('Chat with Sarah')
              ],
            ),
          ),
          Row(
            children: [
              Icon(
                Icons.person,
                size: 40,
              ),
              Column(
                children: [Text('Hello Iris'), Text('Good to meet you')],
              )
            ],
          ),
          Padding(
            padding: const EdgeInsets.symmetric(
              vertical: 20,
            ),
            child: Padding(
              padding: const EdgeInsets.only(left: 450),
              child: Positioned(
                right: 0,
                child: Row(
                  children: [
                    Column(
                      children: [Text('Hello Sarah'), Text('How are you')],
                    ),
                    Icon(
                      Icons.person,
                      size: 40,
                    ),
                  ],
                ),
              ),
            ),
          )
        ],
      ),
    );
  }
}
