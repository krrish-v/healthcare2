import 'package:carousel_slider/carousel_slider.dart';
import 'package:flutter/material.dart';
import 'package:material_design_icons_flutter/material_design_icons_flutter.dart';

class Caro extends StatefulWidget {
  const Caro({Key? key}) : super(key: key);

  @override
  State<Caro> createState() => _CaroState();
}

class _CaroState extends State<Caro> {
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
                const Text('create avatar')
              ],
            ),
          ),
          Expanded(
              child: CarouselSlider(
            options: CarouselOptions(height: 400.0),
            items: [
              Icon(
                MdiIcons.humanMale,
                size: 50,
              ),
              Icon(
                MdiIcons.humanFemale,
                size: 50,
              ),
              Icon(
                MdiIcons.octahedron,
                size: 50,
              )
            ].map((i) {
              return Builder(
                builder: (BuildContext context) {
                  return Center(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Container(
                            width: 200,
                            height: 300,
                            margin: EdgeInsets.symmetric(horizontal: 5.0),
                            decoration: BoxDecoration(color: Colors.amber),
                            child: i),
                        SizedBox(
                          height: 20,
                        ),
                        Text("Select Gender")
                      ],
                    ),
                  );
                },
              );
            }).toList(),
          ))
        ],
      ),
    );
  }
}
