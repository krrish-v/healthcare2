import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_health/setting/symptonques.dart';

import '../caro.dart';
import 'buddymatch.dart';

class Settings extends StatefulWidget {
  const Settings({Key? key}) : super(key: key);

  @override
  State<Settings> createState() => _SettingsState();
}

class _SettingsState extends State<Settings> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Column(children: [
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
            const Text('User Setting')
          ],
        ),
      ),
      Stack(
        children: [
          Container(
              height: 140,
              width: 140,
              child: const Icon(
                Icons.person,
                size: 100,
              )),
          Positioned(
              right: 3,
              child: IconButton(
                  onPressed: () {},
                  icon: const Icon(
                    Icons.edit,
                    size: 14,
                  )))
        ],
      ),
      const Text('Name'),
      const SizedBox(
        height: 20,
      ),
      const Icon(Icons.location_on_rounded),
      const SizedBox(
        height: 50,
      ),
      Padding(
        padding: const EdgeInsets.symmetric(vertical: 40),
        child: InkWell(
          onTap: () {
            Navigator.of(context)
                .push(CupertinoPageRoute(builder: (cintext) => Caro()));
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
                  child: Icon(Icons.settings),
                ),
                SizedBox(
                  width: 30,
                ),
                Text(
                  'Avatar Creation',
                  style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold),
                ),
              ],
            ),
          ),
        ),
      ),
      Padding(
        padding: const EdgeInsets.only(top: 0),
        child: InkWell(
          onTap: () {
            Navigator.push(
                context, MaterialPageRoute(builder: ((context) => SymQues())));
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
                  child: Icon(Icons.edit),
                ),
                SizedBox(
                  width: 30,
                ),
                Text(
                  'Symptom Questionnaire',
                  style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold),
                ),
              ],
            ),
          ),
        ),
      ),
      Padding(
        padding: const EdgeInsets.symmetric(vertical: 40),
        child: InkWell(
          onTap: () {
            Navigator.of(context)
                .push(MaterialPageRoute(builder: (context) => BuddyMatch()));
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
                  child: Icon(Icons.people),
                ),
                SizedBox(
                  width: 30,
                ),
                Text(
                  'My Buddy Contacts',
                  style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold),
                ),
              ],
            ),
          ),
        ),
      ),
      Container(
        height: 50,
        width: 350,
        decoration: const BoxDecoration(
          borderRadius: BorderRadius.all(Radius.circular(0)),
          color: Colors.grey,
        ),
        child: Row(
          children: const [
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 10),
              child: Icon(Icons.subscriptions),
            ),
            SizedBox(
              width: 30,
            ),
            Text(
              'My Subscription Plan',
              style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      )
    ]));
  }
}
