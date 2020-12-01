import React from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col';


class Alarm extends React.Component {

    calculateCatergory(probability) {
        if (probability >= 95) { return ["critical", '#E94D4D'] }
        else if (probability >= 85) { return ["major", '#FF994F'] }
        else { return ["minor", '#EDC535'] };
    }

    calculateDate(timestamp) {
        let now = new Date(timestamp);
        let year = now.getFullYear();
        var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        let month = months[now.getMonth()];
        let day = now.getDate();
        let hours = now.getHours();
        let minutes = now.getMinutes();
        let seconds = now.getSeconds();
        let time = (hours < 10 ? "0" + hours.toString() : hours.toString()) + ":" + (minutes < 10 ? "0" + minutes.toString() : minutes.toString()) + ":" + (seconds < 10 ? "0" + seconds.toString() : seconds.toString());
        let date = (day < 10 ? "0" + day.toString() : day.toString()) + "." + month + "." + year;
        return [`${date}`, `${time}`]
    }

    render() {
        return (
            <Card>

                <Card.Header>
                    <Accordion.Toggle as={Card.Header} class="p-0" eventKey={this.props.data}>
                        <Row>
                            <h5 class="font-weight-lighter ml-2 mt-n2">Alarm #{this.props.data.id}</h5>
                        </Row>
                        <Row>
                            <h3 class="ml-2 mb-n1 font-weight-light">{this.props.data.suspectedAttackType}</h3>
                            <div class="tag ml-2 mt-1" style={{ "background-color": this.calculateCatergory(this.props.data.probability)[1] }}>
                                &#8205; &#8205; {this.calculateCatergory(this.props.data.probability)[0]} &#8205; &#8205;
                            </div>
                            <div class="text-right w-100 mt-n4">
                                {this.calculateDate(this.props.data.time)[0]} {this.calculateDate(this.props.data.time)[1]}
                            </div>
                        </Row>
                    </Accordion.Toggle>
                </Card.Header>

                <Accordion.Collapse eventKey={this.props.data}>
                    <Card.Body style={{ "border-color": "red" }}>
                        <Row>
                            <Col>
                                <Row><h6 class="ml-2 mt-n2">Propability</h6></Row>
                                <Row><h2 class="ml-2 mt-n2 font-weight-lighter">{this.props.data.probability}%</h2></Row>
                                <Row><h6 class="ml-2">Affected Systems</h6></Row>
                                <Row><h2 class="ml-2 mt-n2 font-weight-lighter">{this.props.data.affectedSystems.join(', ')}</h2></Row>
                                <Row><h6 class="ml-2">Automatic Reaction</h6></Row>
                                <Row><h2 class="ml-2 mt-n2 mb-n2 font-weight-lighter">{this.props.data.automaticReaction.length !== 0 ? this.props.data.automaticReaction.join(", ") : "None"}</h2></Row>
                            </Col>
                            <Col>
                                <h6 class="mt-n2">Checklist</h6>
                                <Form.Group controlId="formBasicCheckbox" class="mb-n2">
                                    {this.props.data.checklist.map(check => {
                                        return <Form.Check type="checkbox" label={<h4 class="font-weight-lighter">{check}</h4>} id={check} />
                                    })}
                                </Form.Group>
                            </Col>
                        </Row>
                    </Card.Body>
                </Accordion.Collapse>
            </Card >);
    }
}

export default Alarm;
