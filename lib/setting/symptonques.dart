import 'package:flutter/material.dart';

class SymQues extends StatefulWidget {
  SymQues({Key? key}) : super(key: key);

  @override
  State<SymQues> createState() => _SymQuesState();
}

class _SymQuesState extends State<SymQues> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 30),
            child: Row(
              children: [
                IconButton(
                  icon: const Icon(Icons.arrow_back),
                  onPressed: () {
                    Navigator.of(context).pop();
                  },
                ),
                const SizedBox(
                  width: 200,
                ),
                const Text('Symptom Questionnaire')
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 20),
            child: Column(
              children: [
                const Text('Question 1'),
                Container(
                  height: 50,
                  width: 400,
                  decoration: BoxDecoration(color: Colors.grey),
                  child: TextFormField(),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 20),
            child: Column(
              children: [
                const Text('Question 2'),
                Container(
                  height: 50,
                  width: 400,
                  decoration: BoxDecoration(color: Colors.grey),
                  child: TextFormField(),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 20),
            child: Column(
              children: [
                Text('Question 3'),
                Container(
                  height: 50,
                  width: 400,
                  decoration: BoxDecoration(color: Colors.grey),
                  child: TextFormField(),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 20),
            child: Column(
              children: [
                const Text('Question 4'),
                Container(
                  height: 50,
                  width: 400,
                  decoration: BoxDecoration(color: Colors.grey),
                  child: TextFormField(),
                ),
              ],
            ),
          ),
          SizedBox(
            height: 100,
          ),
          Container(
            height: 45,
            width: 250,
            color: Colors.black,
            child: ElevatedButton(onPressed: () {}, child: Text('Submit')),
          )
        ],
      ),
    );
  }
}
