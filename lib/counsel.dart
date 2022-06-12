import 'package:flutter/material.dart';

import 'package:material_design_icons_flutter/material_design_icons_flutter.dart';

import 'counsellor.dart';

class Counsellor extends StatefulWidget {
  Counsellor({Key? key}) : super(key: key);

  @override
  State<Counsellor> createState() => _CounsellorState();
}

class _CounsellorState extends State<Counsellor> {
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
                  'We have found 2 Counsellors nearby',
                  style: TextStyle(fontWeight: FontWeight.bold),
                ),
              ],
            ),
          ),
          Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Container(
                height: 150,
                width: MediaQuery.of(context).size.width,
                color: Colors.red,
                child: Card(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: <Widget>[
                      Icon(
                        MdiIcons.humanChild,
                        size: 100,
                      ),
                      Text('Dr Joyce'),
                      Expanded(
                          child: Container(
                        padding: const EdgeInsets.all(5),
                        child: Column(
                          children: [
                            Center(
                                child: Padding(
                              padding: EdgeInsets.only(top: 50),
                              child: Container(
                                  height: 50,
                                  width: 100,
                                  color: Colors.blue,
                                  child: Center(child: Text('Connect'))),
                            ))
                          ],
                        ),
                      ))
                    ],
                  ),
                ),
              ),
              SizedBox(
                height: 50,
              ),
              Container(
                height: 150,
                width: MediaQuery.of(context).size.width,
                color: Colors.blue,
                child: Card(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: <Widget>[
                      Icon(
                        MdiIcons.humanChild,
                        size: 100,
                      ),
                      Text('Dr Joyce'),
                      Expanded(
                          child: Container(
                        padding: const EdgeInsets.all(5),
                        child: Column(
                          children: [
                            Center(
                                child: Padding(
                              padding: EdgeInsets.only(top: 50),
                              child: InkWell(
                                onTap: () {
                                  Navigator.of(context).push(MaterialPageRoute(
                                      builder: (context) => Joyce()));
                                },
                                child: Container(
                                    height: 50,
                                    width: 100,
                                    color: Colors.blue,
                                    child: Center(child: Text('Connect'))),
                              ),
                            ))
                          ],
                        ),
                      ))
                    ],
                  ),
                ),
              ),
              SizedBox(
                height: 50,
              ),
              Container(
                height: 150,
                width: MediaQuery.of(context).size.width,
                color: Colors.black,
                child: Card(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: <Widget>[
                      Icon(
                        MdiIcons.humanChild,
                        size: 100,
                      ),
                      Text('Dr Joyce'),
                      Expanded(
                          child: Container(
                        padding: const EdgeInsets.all(5),
                        child: Column(
                          children: [
                            Center(
                                child: Padding(
                              padding: EdgeInsets.only(top: 50),
                              child: Container(
                                  height: 50,
                                  width: 100,
                                  color: Colors.blue,
                                  child: Center(child: Text('Connect'))),
                            ))
                          ],
                        ),
                      ))
                    ],
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
