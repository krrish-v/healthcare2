import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_health/signup.dart';

class Welcome extends StatefulWidget {
  const Welcome({Key? key}) : super(key: key);

  @override
  State<Welcome> createState() => _WelcomeState();
}

class _WelcomeState extends State<Welcome> {
  @override
  void initState() {
    super.initState();
    Future.delayed(Duration(seconds: 2)).then((value) => Navigator.of(context)
        .push(CupertinoPageRoute(builder: (context) => SignUp())));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              'Welcome',
              style: TextStyle(fontSize: 30),
            ),
            Icon(Icons.face_retouching_natural_sharp, size: 100)
          ],
        ),
      ),
    );
  }
}
