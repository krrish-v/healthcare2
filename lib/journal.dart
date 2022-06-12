import 'package:flutter/material.dart';

class Journal extends StatefulWidget {
  Journal({Key? key}) : super(key: key);

  @override
  State<Journal> createState() => _JournalState();
}

class _JournalState extends State<Journal> {
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
                const Text('Mood journal')
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 40, horizontal: 60),
            child: Row(
              children: [
                Text(
                  'Sunday 12 June 2022',
                  style: TextStyle(fontWeight: FontWeight.bold),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 40, horizontal: 60),
            child: Row(
              children: [
                Text(
                  'What Have you been Up to today?',
                  style: TextStyle(fontWeight: FontWeight.bold),
                ),
              ],
            ),
          ),
          TextFormField(),
          TextFormField(),
          TextFormField(),
          SizedBox(
            height: 30,
          ),
          Text('select your mood'),
          SizedBox(
            height: 30,
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [Icon(Icons.face), Icon(Icons.face), Icon(Icons.face)],
          )
        ],
      ),
    );
  }
}
