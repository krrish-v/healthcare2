import 'package:flutter/material.dart';

class Joyce extends StatefulWidget {
  Joyce({Key? key}) : super(key: key);

  @override
  State<Joyce> createState() => _JoyceState();
}

class _JoyceState extends State<Joyce> {
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
            const Text('Dr Joyce Ghee')
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
          // Positioned(
          //     right: 3,
          //     child: IconButton(
          //         onPressed: () {},
          //         icon: const Icon(
          //           Icons.edit,
          //           size: 14,
          //         )))
        ],
      ),
      const Text('Dr Joyce Ghee'),
      const Text('Counsellor'),
      const SizedBox(
        height: 20,
      ),
      const Icon(Icons.location_on_rounded),
      const SizedBox(
        height: 50,
      ),
      // Padding(
      //     padding: const EdgeInsets.symmetric(vertical: 40),
      //     child: Container(
      //       height: 50,
      //       width: 350,
      //       decoration: const BoxDecoration(
      //         borderRadius: BorderRadius.all(Radius.circular(0)),
      //         color: Colors.grey,
      //       ),
      //       // child: Row(
      //       //   children: const [
      //       //     Padding(
      //       //       padding: EdgeInsets.symmetric(horizontal: 10),
      //       //       child: Icon(Icons.settings),
      //       //     ),
      //       //   ],
      //       // ),
      //     )),
      Padding(
        padding: const EdgeInsets.symmetric(vertical: 40, horizontal: 20),
        child: Text(
            'counselling can offer you a space to explore challenges in a supportive and non judgemental environment Dr.Ghee can assist you to lead a more rewarding and fulfilling life'),
      ),
      Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Icon(Icons.email),
          Icon(Icons.chat),
          Icon(Icons.call),
          Icon(Icons.video_call),
        ],
      )
    ]));
  }
}
