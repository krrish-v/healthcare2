import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'home.dart';

class SignUp extends StatefulWidget {
  const SignUp({Key? key}) : super(key: key);

  @override
  State<SignUp> createState() => _SignUpState();
}

class _SignUpState extends State<SignUp> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Padding(
                padding: const EdgeInsets.only(left: 40, right: 40),
                child: TextFormField(
                  decoration: InputDecoration(labelText: 'email'),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(left: 40, right: 40),
                child: TextFormField(
                  decoration: InputDecoration(labelText: 'password'),
                ),
              ),
              ElevatedButton(
                  onPressed: () {
                    Navigator.of(context).push(
                        CupertinoPageRoute(builder: (context) => MyHomePage()));
                  },
                  child: Text('Sign up'))
            ],
          ),
        ),
      ),
    );
  }
}
