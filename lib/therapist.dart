import 'package:flutter/material.dart';

import 'counsel.dart';

class Therapist extends StatefulWidget {
  Therapist({Key? key}) : super(key: key);

  @override
  State<Therapist> createState() => _TherapistState();
}

class _TherapistState extends State<Therapist> {
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
                const Text('Find a Therapist')
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 40, horizontal: 60),
            child: Row(
              children: [
                Text(
                  'What Kind of help do you need ?',
                  style: TextStyle(fontWeight: FontWeight.bold),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 40),
            child: InkWell(
              onTap: () {
                Navigator.of(context).push(
                    MaterialPageRoute(builder: (context) => Counsellor()));
              },
              child: Container(
                height: 50,
                width: 350,
                decoration: const BoxDecoration(
                  borderRadius: BorderRadius.all(Radius.circular(0)),
                  color: Colors.grey,
                ),
                child: Row(
                  children: const [
                    Padding(
                      padding: EdgeInsets.symmetric(horizontal: 10),
                      // child: Icon(Icons.settings),
                    ),
                    SizedBox(
                      width: 30,
                    ),
                    Center(
                      child: Text(
                        'Counsellor',
                        style: TextStyle(
                            fontSize: 17, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 20),
            child: Container(
              height: 50,
              width: 350,
              decoration: const BoxDecoration(
                borderRadius: BorderRadius.all(Radius.circular(0)),
                color: Colors.grey,
              ),
              child: Row(
                children: const [
                  Padding(
                    padding: EdgeInsets.symmetric(horizontal: 10),
                    // child: Icon(Icons.settings),
                  ),
                  SizedBox(
                    width: 30,
                  ),
                  Center(
                    child: Text(
                      'Licensed Therapist',
                      style:
                          TextStyle(fontSize: 17, fontWeight: FontWeight.bold),
                    ),
                  ),
                ],
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 20),
            child: Container(
              height: 50,
              width: 350,
              decoration: const BoxDecoration(
                borderRadius: BorderRadius.all(Radius.circular(0)),
                color: Colors.grey,
              ),
              child: Row(
                children: const [
                  Padding(
                    padding: EdgeInsets.symmetric(horizontal: 10),
                    // child: Icon(Icons.settings),
                  ),
                  SizedBox(
                    width: 30,
                  ),
                  Center(
                    child: Text(
                      'Social Worker',
                      style:
                          TextStyle(fontSize: 17, fontWeight: FontWeight.bold),
                    ),
                  ),
                ],
              ),
            ),
          ),
          Text('please select a SUBSCRIPTION PlAN to proceed')
        ],
      ),
    );
  }
}
